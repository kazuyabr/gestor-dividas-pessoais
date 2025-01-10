export interface Divida {
    id: number;
    titulo: string;
    valor: number;
    data_vencimento: string;
    status: DividaStatus;
    observacoes?: string;
    created_at: string;
    updated_at: string;
}

export type DividaStatus = 'PENDENTE' | 'PAGO' | 'ATRASADO';

export interface DividaCreate {
    titulo: string;
    valor: number;
    data_vencimento: string;
    status: DividaStatus;
    observacoes?: string;
}

export interface DividaUpdate extends Partial<DividaCreate> {}

export interface DividaFiltros {
    status?: DividaStatus;
    ordenacao?: 'asc' | 'desc';
    campo?: keyof Divida;
}
