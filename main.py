import flet as ft

from conection import Conectar


def main(page: ft.Page):
    page.title = "Gestión de Clientes"
    conexion = Conectar()
   
   #crear campos de input para agregar clientes
    campo_dni= ft.TextField(label="DNI")
    campo_nombre= ft.TextField(label="Nombre")
    campo_apellido= ft.TextField(label="Apellido")
    campo_tel= ft.TextField(label="Telefono")
    campo_fecha= ft.TextField(label="Fecha nac. (YYYY-MM-DD)")
    #---------- crear Tabla clientes------------------
    tabla_clientes= ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("DNI")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Apellido")),
            ft.DataColumn(ft.Text("Telefono")),
            ft.DataColumn(ft.Text("Fecha Nacimiento")),
            ft.DataColumn(ft.Text("Botones")),
        ],
        rows=[],
    )
    def cargar_cliente():
        tabla_clientes.rows.clear()
        for cliente in conexion.obtener_cliente():
            tabla_clientes.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(cliente["id_cliente"]))),
                        ft.DataCell(ft.Text(str(cliente["DNI"]))),
                        ft.DataCell(ft.Text(cliente["nombre"])),
                        ft.DataCell(ft.Text(cliente["apellido"])),
                        ft.DataCell(ft.Text(str(cliente["tel"]))),
                        ft.DataCell(ft.Text(str(cliente["fecha_nac"]))),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.Icons.DELETE,data=cliente["id_cliente"], on_click=eliminar_cliente
                                                  ),
                                    ft.IconButton(icon=ft.Icons.EDIT, data=cliente, on_click=seleccionar_cliente)])
                        ),
                    ]
                )
            )
            page.update()
    #-----------------funcion para el boton-----------------
    def agregar_clienteClick(e):
        conexion.agregar_cliente(
            campo_dni.value,
            campo_nombre.value,
            campo_apellido.value,
            campo_tel.value,
            campo_fecha.value,
        )
        #------------limpiar formulario------------
        campo_dni.value = ""
        campo_nombre.value = ""
        campo_apellido.value = ""
        campo_tel.value = ""
        campo_fecha.value = ""

        cargar_cliente()

    def eliminar_cliente(e):
        conexion.eliminar_cliente(e.control.data)
        cargar_cliente()
        
    def seleccionar_cliente(e):
        campo_dni.value=str(e.control.data["DNI"])
        # campo_nombre.value=(cliente["nombre"])
        # campo_apellido.value=(cliente["apellido"])
        # campo_tel.value=str(cliente["tel"])
        # campo_fecha.value=str(cliente["fecha_nac"])
      
    # def guardar_edicion(e):
    #     conexion.editar_cliente(campo_dni.value,
    #         campo_nombre.value,
    #         campo_apellido.value,
    #         campo_tel.value,
    #         campo_fecha.value,)
    #     page.update()
        


    vista_clientes=ft.Column(
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Row(
                controls=[
                    campo_dni,
                    campo_nombre,
                    campo_apellido,
                    campo_tel,
                    campo_fecha]),
                    ft.Button("Guardar", on_click=agregar_clienteClick),
                    tabla_clientes,
        ]
    )

    cargar_cliente()

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Tabs(
                length=3,
                selected_index=0,
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[
                        ft.TabBar(
                            tabs=[
                                ft.Tab(label="Productos"),
                                ft.Tab(label="Pedidos"),
                                ft.Tab(label="Clientes"),
                            ],
                        ),
                        ft.TabBarView(
                            expand=True,
                            controls=[
                                ft.Text("Acá van los productos"),
                                ft.Text("Acá van los pedidos"),
                                vista_clientes,
                            ],
                        ),
                    ],
                ),
            ),
        )
    )

ft.run(main)