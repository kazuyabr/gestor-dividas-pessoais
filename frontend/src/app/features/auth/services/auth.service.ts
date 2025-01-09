import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { User, UserLogin, UserRegister } from '../interfaces/user.interface';
import { Router } from '@angular/router';
import { environment } from '../../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private currentUserSubject = new BehaviorSubject<User | null>(null);
  public currentUser$ = this.currentUserSubject.asObservable();
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router) {}

  login(credentials: UserLogin): Observable<User> {
    return this.http.post<User>('/usuarios/login', credentials).pipe(
      tap(user => this.currentUserSubject.next(user))
    );
  }

  register(userData: UserRegister): Observable<User> {
    return this.http.post<User>(`${this.apiUrl}/usuarios/`, userData);
  }

  logout(): void {
    this.currentUserSubject.next(null);
  }

  isAuthenticated(): boolean {
    return !!this.currentUserSubject.value;
  }

  redirectToLogin(): void {
    this.router.navigate(['/auth/login']);
  }
}
