$(document).ready(function() {

    // Toggle edit-mode
    $('#edit-relations').on('click', function() {
        if ($(this).hasClass('active')) {
            $('.relation_toolbar').css('display', 'none');
            $('#relation-form').slideUp();
            $(this).text('Redigér relationer');
        } else {
            $('.relation_toolbar').css('display', 'inline-block');
            $(this).text('Afslut relationsredigering');
        }
        $(this).toggleClass('active');
    });

    // Click on single relations_toolbar
    $('.relation_action').on('click', function(e) {
        e.preventDefault();
        if ($(this).attr('data-action') == 'create') {
            var anchor = $(this).closest('.media');
            $('#relation-form').detach().appendTo(anchor).show();
        } else if ($(this).attr('data-action') == 'delete') {
            var relation_id = $(this).closest('.relation').attr('id');
            $.ajax({
                url: '/relations/' + relation_id,
                dataType: 'json',
                method: 'DELETE'
            })
            .done(function(response) {
                console.log(response);
                $('div[id= ' + relation_id + ']').slideUp(500, function() {
                    $(this).remove();
                });
            })
            .fail(function(error) {
                alert(error);
            });        
        }
    });

    // Relationsform kan kun create
    $('#relation-form').on('submit', function() {
        $.ajax({
            url: '/relations',
            dataType: 'json',
            method: 'POST',
            data: $(this).serialize()
        })
        .done(function(response) {
            $('#relation-form').slideUp(500, function() {
                $('#relation-form input').each( function(i) {
                    // Reset values from all label and object-fields
                    if ( ['rel_label', 'object_label', 'object_id', 'object_domain'].indexOf( $(this).attr('name') ) > -1) {
                        $(this).val(" ");
                    }
                });
            });
        })
        .fail(function(error) {
            alert(error);
        });
        return false;
    });

});