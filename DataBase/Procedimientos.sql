-- CRUD TABLA clientes

-- Crear
-- Crear
create or replace function crear_usuario_f2(
    id_usuario ventas.clientes.idcliente%type,
    nombre_usuario ventas.clientes.nomcliente%type,
    direccion_usuario ventas.clientes.dircliente%type,
    pais_usuario ventas.clientes.idpais%type,
    telefono_usuario ventas.clientes.fonocliente%type
)
returns void as
$$
begin 
	
    insert into ventas.clientes (
        idcliente,
        nomcliente,
        dircliente,
        idpais,
        fonocliente
    )
    values (
        id_usuario, 
        nombre_usuario,
        direccion_usuario, 
        pais_usuario, 
        telefono_usuario
    );

    RAISE NOTICE 'Usuario Ingresado';
	
    RAISE NOTICE 'ID Cliente: %, Nombre: %, Dirección: %,  idPais: %, Teléfono: %',
        id_usuario, nombre_usuario, direccion_usuario, pais_usuario, telefono_usuario;
	
    RETURN;
END
$$
LANGUAGE plpgsql;


select * from ventas.clientes c 

select crear_usuario_f2('Ga65', 'pepe','ul. Filtrowa 68', '002', '(26); 642-7012')

-- Leer (Mostar)

create or replace function mostrar_usuario_f()
returns table (idcliente ventas.clientes.idcliente%type, nomcliente ventas.clientes.nomcliente%type,
               dircliente ventas.clientes.dircliente%type, idpais ventas.clientes.idpais%type,
               fonocliente ventas.clientes.fonocliente%type)
as 
$$
begin 
    return query
    select c.idcliente, c.nomcliente, c.dircliente, c.idpais, c.fonocliente
    from ventas.clientes c;
end;
$$
LANGUAGE 'plpgsql';

select * from mostrar_usuario_f();


-- Actualizar


create or replace procedure actualizar_usuario (
		id_usuario ventas.clientes.idcliente%type,
		nombre_usuario ventas.clientes.nomcliente%type,
		direcion_usuario ventas.clientes.dircliente%type,
		pais_usuario ventas.clientes.idpais%type,
		telefono_usuario ventas.clientes.fonocliente%type
)
as
$$
begin 
	
	update ventas.clientes  set
	nomcliente = nombre_usuario,
	dircliente = direcion_usuario,
	idpais = pais_usuario,
	fonocliente = telefono_usuario
	where idcliente = id_usuario;
	RAISE NOTICE 'Usuario Actualizado';
	
	RAISE NOTICE 'ID Cliente: %, Nombre: %, Dirección: %,  idPais: %, Teléfono: %',
            id_usuario, nombre_usuario, direcion_usuario,pais_usuario,telefono_usuario;
END;
$$
LANGUAGE 'plpgsql';

call actualizar_usuario('Gaa1', 'PEPE LUIS','ul. Filtrowa 68', '002', '(26); 642-7012')

select * from ventas.clientes c 

-- Eliminar


create or replace procedure eliminar_usuario (
	id_usuario ventas.clientes.idcliente%type
)
as
$$
begin 
	delete from ventas.clientes
	where idcliente = id_usuario;
	RAISE NOTICE 'Usuario Elimnado';
END;
$$
LANGUAGE 'plpgsql';

call eliminar_usuario('Gaa')

select * from ventas.clientes c 


