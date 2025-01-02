export interface User {
    id: number;
    nome: string;
    email: string;
}

export interface UserLogin {
    email: string;
    senha: string;
}

export interface UserRegister {
    nome: string;
    email: string;
    senha: string;
}
