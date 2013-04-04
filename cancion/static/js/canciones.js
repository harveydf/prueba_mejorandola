$(document).on('ready', main_cancion);

function main_cancion() {
	$('#cancion-id #eliminar').on('click', eliminar_cancion);
	$('#cancelar').on('click', ocultar_form);
	$('#nuevo').on('click', mostrar_form);
	$('#editar').on('click', mostrar_form);
}

function eliminar_cancion() {
	eliminar = confirm('¿Está seguro que desea eliminar esta canción?');

	if(eliminar){
		$.get('/cancion/eliminar/' + $('#cancion-id').data('id'), function (data) {
			if(data.redirect) {
				window.location.href = data.redirect;
			}
			else if(data.error){
				alert(data.error);
			}
		});
	}
}

function ocultar_form() {
	$('form').hide();
}

function mostrar_form(){
	$('form').show();
}