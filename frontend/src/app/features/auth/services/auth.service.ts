import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, catchError, Observable, tap } from 'rxjs';
import { environment } from '../../../../environments/environment';
import { AuthToken } from '../interfaces/auth.interface';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = `${environment.apiUrl}:${environment.apiPort}/api/${environment.apiVersion}`;
  private tokenSubject = new BehaviorSubject<string | null>(localStorage.getItem('token'));
  private refreshTokenTimeout: any;

  constructor(private http: HttpClient) {
    this.startRefreshTokenTimer();
  }

  register(userData: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/usuarios`, userData);
  }

  login(credentials: {username: string, password: string}): Observable<AuthToken> {
    const formData = new FormData();
    formData.append('username', credentials.username);
    formData.append('password', credentials.password);

    return this.http.post<AuthToken>(`${this.baseUrl}/auth/token`, formData).pipe(
      tap(response => {
        localStorage.setItem('token', response.access_token);
        this.tokenSubject.next(response.access_token);
      }),
      catchError(error => {
        console.log('Erro na autenticação:', error);
        throw error;
      })
    );
  }

  logout(): void {
    localStorage.removeItem('token');
    this.tokenSubject.next(null);
    this.stopRefreshTokenTimer();
  }

  getToken(): string | null {
    return this.tokenSubject.value;
  }

  isAuthenticated(): boolean {
    return !!this.getToken();
  }

  private startRefreshTokenTimer() {
    const token = this.tokenSubject.value;
    if (token) {
      const timeout = 1000 * 60 * 14; // 14 minutos
      this.refreshTokenTimeout = setTimeout(() => this.refreshToken().subscribe(), timeout);
    }
  }

  private stopRefreshTokenTimer() {
    clearTimeout(this.refreshTokenTimeout);
  }

  private refreshToken(): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.baseUrl}/auth/refresh-token`, {}).pipe(
      tap(response => {
        localStorage.setItem('token', response.access_token);
        this.tokenSubject.next(response.access_token);
        this.startRefreshTokenTimer();
      })
    );
  }
}
