import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { DividasService } from './dividas.service';

describe('DividasService', () => {
  let service: DividasService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [DividasService]
    });
    service = TestBed.inject(DividasService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('deve listar dívidas', () => {
    service.listarDividas().subscribe();
    const req = httpMock.expectOne('/dividas/');
    expect(req.request.method).toBe('GET');
  });
});
