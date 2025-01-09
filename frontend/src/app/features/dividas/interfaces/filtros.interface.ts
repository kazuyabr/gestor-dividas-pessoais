export interface FiltrosDivida {
  status: '' | 'Pendente' | 'Pago' | 'Atrasado';
  ordenacao: 'asc' | 'desc';
  campo: keyof Divida;
}
