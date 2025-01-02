export interface DashboardSummary {
    totalDividas: number;
    totalValorPendente: number;
    dividasPagas: number;
    dividasVencidas: number;
}

export interface DividaResumo {
    id: number;
    titulo: string;
    valor: number;
    dataVencimento: string;
    status: 'Pendente' | 'Pago' | 'Atrasado';
}
