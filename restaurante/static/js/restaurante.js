$(document).on('ready', main_restaurante);

function main_restaurante() {
	$('#restaurante-id #eliminar').on('click', eliminar_restaurante);
	$('#cancelar').on('click', ocultar_form);
	$('#nuevo').on('click', mostrar_form);
	$('#editar').on('click', mostrar_form);
}

function eliminar_restaurante() {
	eliminar = confirm('¿Está seguro que desea eliminar este restaurante?');

	if(eliminar){
		$.get('/restaurante/eliminar/' + $('#restaurante-id').data('id'), function (data) {
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