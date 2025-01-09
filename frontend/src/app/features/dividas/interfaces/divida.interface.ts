export interface Divida {
    id: number;
    titulo: string;
    valor: number;
    dataVencimento: string;
    status: 'Pendente' | 'Pago' | 'Atrasado';
    observacoes?: string;
    usuario_id: number;
}

export interface DividaCreate {
    titulo: string;
    valor: number;
    dataVencimento: string;
    status: 'Pendente' | 'Pago' | 'Atrasado';
    observacoes?: string;
}

export interface FiltrosDivida {
    status?: string;
    ordenacao?: 'asc' | 'desc';
    campo?: 'titulo' | 'valor' | 'dataVencimento';
}
