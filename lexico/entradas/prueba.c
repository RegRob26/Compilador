-
int menu_principal();
int menu_editar();
int menu_reproducir();
int case_principal(int, Dlinked_list *dlinked_list, int, int, int);
int case_reproducir(int, Dlinked_list *dlinked_list, int *contador);
int case_editar(int, int, Dlinked_list *dlinked_list, int *, int *);

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

int menu_principal()
{
    limpiar_pantalla();
    int option;
    printf("\n");
    printf( "\t\t\tMenú principal\n\n" );
    printf("1.- Editar Lista\n");
    printf("2.- Reproducir \n");
    printf("3.- Salir\n");
        scanf("%d", &option);
    return option;
}

int case_principal(int opcion, Dlinked_list *dlinked_list, int contador, int secuencia, int use)
{
    int bandera_salida, exit;
    switch (opcion)
    {
    case 1:
        do
        {
            bandera_salida = menu_editar();
            exit = case_editar(bandera_salida, 1, dlinked_list, &contador, &use);
        } while (exit != 4);

        break;
    case 2:
        do
        {
            exit = case_reproducir(bandera_salida, dlinked_list, &secuencia);

        } while (exit != 4);
        break;
    case 3:
        sleep(2);
        sleep(2);
        limpiar_pantalla();
        printf("\n");
        break;
    default:
        printf("Reiniciando reproductor...\n");
        break;
    }
    return 0;
}

int menu_editar()
{
    int option;
    limpiar_pantalla();
    printf( "\n\n\tMenú de Edición\n\n" );
    printf( "\t\t\tMenú principal\n\n" );
    printf("1.- Agregar Cancion\n");
    printf("2.- Eliminar cancion \n");
    printf("3.- Mostrar lista \n");
    printf("4.- Salir\n");
    printf("5.- Mostrar lista Ordenada \n");
    printf("6.- Buscar \n");
    scanf("%d", &option);
    limpiar_pantalla();
    return option;
}

int case_editar(int opcion, int eleccion, Dlinked_list *dlinked_list, int *conta, int *use)
{

    int item;
    int i;
    int type;
    int delete;
    fflush(stdin);
    int select = 0;
    FILE *song_all_data;
    char coma;
    int contador = 1;
    song_all_data = fopen("/mnt/c/users/vix/desktop/project2/src/songs_all.txt", "r+");
    //song_all_data = fopen("/home/regrobles/Multimedia/Documentos_X9/project2/src/songs_all.txt", "r+");
    size_t orgpos;
    switch (opcion)
    {
    case 1:
        if (eleccion == 0)
        {
            if (song_all_data == NULL)
            {
                printf("ERROR");
                return 0;
            }
            else
            {

                int cont_may = 0;
                int cont_2 = 0;
                char cancion2[TAM];
                char autor2[TAM];
                char identificador[TAM];
                char anio[TAM];
                char album[TAM];
                char duracion[TAM];
                while (!feof(song_all_data))
                {
                    if (cont_may < 6)
                    {

                        coma = fgetc(song_all_data);
                        if (coma == ',')
                        {
                            char cadena_lectura[contador];
                            orgpos = ftell(song_all_data);
                            fseek(song_all_data, -contador, SEEK_CUR);
                            fgets(cadena_lectura, contador, song_all_data);
                            if (cont_may == 0)
                                strcpy(identificador, cadena_lectura);
                            if (cont_may == 1)
                                strcpy(album, cadena_lectura);
                            if (cont_may == 2)
                                strcpy(autor2, cadena_lectura);
                            if (cont_may == 3)
                                strcpy(duracion, cadena_lectura);
                            if (cont_may == 4)
                                strcpy(cancion2, cadena_lectura);
                            if (cont_may == 5)
                                strcpy(anio, cadena_lectura);

                            fseek(song_all_data, orgpos, SEEK_SET);
                            contador = 1;
                            cont_may++;
                        }
                        else
                            contador++;
                    }
                    else
                    {
                        item = (*conta);
                        cont_2 += cont_may;
                        contador = 1;
                        cont_may = 0;
                        insert(&dlinked_list->head, item, select, autor2, cancion2, anio, identificador, album, duracion);
                        (*conta)++;
                    }
                }
                fclose(song_all_data);
                return 1;
            }

            break;
        }
        else
        {
            char cancion[TAM];
            char autor[TAM];
            char cancion2[TAM];
            char autor2[TAM];
            char identificador1[TAM];
            char anio1[TAM];
            char album1[TAM];
            char duracion1[TAM];
            char identificador[TAM];
            char anio[TAM];
            char album[TAM];
            char duracion[TAM];
            select = 1;
            printf( "\t\tAñadiendo datos\n\n" );
            fflush(stdin);
            printf( "Ingrese el ID: " );
            fflush(stdin);
            getchar();
            gets(identificador1);
            strcpy(identificador, identificador1);

            printf( "Ingrese el nombre del autor: " );
            fflush(stdin);
            getchar();
            gets(autor);
            strcpy(autor2, autor);

            printf( "Ingrese el nombre de la canción: " );
            fflush(stdin);
            gets(cancion);
            strcpy(cancion2, cancion);

            printf( "Ingrese el nombre del Albúm: " );
            fflush(stdin);
            getchar();
            gets(album1);
            strcpy(album, album1);

            printf( "Ingrese la duración de la canción: " );
            fflush(stdin);
            gets(duracion1);
            strcpy(duracion, duracion1);

            printf( "Ingrese el año de la canción: " );
            fflush(stdin);
            gets(anio1);
            strcpy(anio, anio1);
            insert(&dlinked_list->head, item, select, autor2, cancion2, anio, identificador, album, duracion);
            (*conta)++;
            break;
        }

    case 2:
        char Delete_string[TAM];
        printf( "\t\tELIMINANDO DATOS...\n\n" );
        printf( "Ingrese el nùmero de la canciòn a eliminar [si desea eliminar por nombre, ingrese -2612]: " );
        scanf("%d", &delete);

        if (delete == -2612)
        {

            printf("Ingrese el nombre de la canción: ");
            getchar();
            gets(Delete_string);
            int del_node = delete_node(&dlinked_list->head, delete, -26, Delete_string);
            if (del_node == INT_MIN)
            {
                printf( "\t\tLista vacía, añada un elemento\n" );
                fflush(stdin);
                getchar();
            }
            else
            {
                if (del_node == INT_MAX)
                {
                    printf( "Elemento no fue encontrado...\n" );
                    getchar();
                }
                else
                {
                    printf( "La canción ha sido eliminada...\n" );
                    getchar();
                }
            }
            getchar();
            getchar();
            break;
        }
        else
        {
            int del_node = delete_node(&dlinked_list->head, delete, 0, "Hola");

            if (del_node == INT_MIN)
            {
                printf( "\t\tLista vacía, añada un elemento\n" );
                fflush(stdin);
                getchar();
            }
            else
            {
                if (del_node == INT_MAX)
                {
                    printf( "Elemento no fue encontrado...\n" );
                    getchar();
                }
                else
                {
                    getchar();
                }
            }
            getchar();
            break;
        }

    case 3:
        limpiar_pantalla();
        printf( "\t\t\tMOSTRANDO ELEMENTOS DE LA LISTA\n\n" );
        display(dlinked_list);
        fflush(stdin);
        getchar();
        break;
    case 4:
        return 4;
        break;
    case 5:
        int item = (*conta);
        printf("%d", item);
        limpiar_pantalla();
        printf("Desea ordenar por ID [1] o por nombre [2]");
        scanf("%d", &type);

        if (type == 1)
        {
            printf( "\t\tORDENANDO ELEMENTOS DE LA LISTA POR ID\n\n" );
            bubble_sort(&dlinked_list->head, item, 1);
        }
        else
        {
            printf( "\t\tORDENANDO ELEMENTOS DE LA LISTA\n\n" );
            bubble_sort(&dlinked_list->head, item, 2);
        }
        (*use) = 1;
        getchar();
        getchar();
        break;
    case 6:
        char Delete_string_2[TAM];
        int tam = (*conta);
        int type;
        int uso = (*use);
        printf( "\nDEsea buscar por nombre[0] o por ID[1]: " );
        scanf("%d", &type);

        if (type == 0)
        {
            printf( "\nIngrese el nombre de la canción a buscar: " );
            getchar();
            gets(Delete_string_2);
            printf( "\t\tBuscando elemento\n" );
            sleep(3);
            limpiar_pantalla();
            search_item(dlinked_list, &dlinked_list->head, Delete_string_2, tam, type, uso);
        }
        else
        {
            printf( "\nIngrese el ID:" );
            getchar();
            gets(Delete_string_2);
            printf( "\t\tBuscando elemento\n" );
            sleep(3);
            limpiar_pantalla();
            search_item(dlinked_list, &dlinked_list->head, Delete_string_2, tam, type, uso);
        }

        break;
    default:
        break;
    }
    return 0;
}

int menu_reproducir()
{
    int option;
    printf("\nreproducir ");
    printf("1.- Play\n");
    printf("2.- Siguiente \n");
    printf("3.- Anterior \n");
    printf("4.- Pausa\n");
    scanf("%d", &option);
    limpiar_pantalla();
    return option;
}

int case_reproducir(int opcion, Dlinked_list *dlinked_list, int *contador)
{
    fflush(stdin);
    limpiar_pantalla();
    reproducir(dlinked_list);
}