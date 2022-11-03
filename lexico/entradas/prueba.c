int menu_principal();
int menu_editar();
int menu_reproducir();
int case_principal(int, Dlinked_list dlinked_list, int, int, int);
int case_reproducir(int, Dlinked_list dlinked_list, int contador);
int case_editar(int, int, Dlinked_list dlinked_list, int , int );

int main(){
    Dlinked_list *dlinked_list = create_dlinked_list();
    int opcion;
    int contador = 1;
    int secuencia = 0;
    int use = 1;
    getchar();
    limpiar_pantalla();
    case_editar(1, 0, dlinked_list, &contador, 0);
    sleep(2.5);
    printf("\n");
    getchar();
    limpiar_pantalla();
    do
    {
        opcion = menu_principal();
        case_principal(opcion, dlinked_list, contador, secuencia, use);

    } while (opcion != 3);
}
