  import { Injectable } from '@angular/core';
  import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
  import { Observable } from 'rxjs';
  import { environment } from '../../../environments/environment';

  @Injectable()
  export class ApiInterceptor implements HttpInterceptor {
    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
      const apiReq = request.clone({
        url: `${environment.apiUrl}${request.url}`,
        setHeaders: {
          'Content-Type': 'application/json'
        }
      });
      return next.handle(apiReq);
    }
  }
