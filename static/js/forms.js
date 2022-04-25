$(document).ready(function() {

    // Action-buttons inside .forms
    $('.form').on('click', 'input[class^="element-"]', function(e) {
        e.preventDefault();
        if ($(this).hasClass('disabled')) {
            return false;
        }

        var $this = $(this);
        var $element = $this.closest('.array-element');
        // var $input = $element.find('input[type="text"]');

        var previous = $element.prev('.array-element').length;
        var next = $element.next('.array-element').length;

        if ( $this.hasClass('element-remove') ) {
            // If an element before or after, slide it up
            // Else reset and disable 'remove'-button
            if (previous || next) {
                $element.slideUp(function() {
                    $element.remove();
                });
            } else {
                $this.siblings('input[type="text"]').removeAttr('value');
                // $this.addClass('disabled');
            }

        } else if ( $this.hasClass('element-add') ) {
            // Clone .array-element
            var $clone = $element.clone();
            // strip value from input-field
            // enable all actions
            // $clone.find('input[class^="element-"]').removeClass('disabled');
            // $clone.find('input[type="text"]').focus();
            // if (!next) {
            //     $clone.find('.element-down').addClass('disabled');
            // }
            $clone.insertAfter($element).find('input[type="text"]').focus();
            $clone.find('input[type="text"]').removeAttr('value');

        } else if ( $this.hasClass('element-up') ) {
            if ( !previous ) {
                return false;
            } else {
                $element.slideUp(function() {
                    var $prev_element = $element.prev('.array-element');
                    $element.detach();
                    $element.insertBefore($prev_element).slideDown();
                });
            }
        } else if ( $this.hasClass('element-down') ) {
            if ( !next ) {
                return false;
            } else {
                $element.slideUp(function() {
                    var $next_element = $element.next('.array-element');
                    $element.detach();
                    $element.insertAfter($next_element).slideDown();
                });
            }
        }

        // var $container = $this.closest('.element');
        // $container.find('input[class^="element-"]').removeClass('disabled');        
        // $container.find('.array-element').filter(':first').find('.element-up').addClass('disabled');
        // $container.find('.array-element').filter(':last').find('.element-down').addClass('disabled');

        // $container.find('.__array-element').each(function(i) {
        //     var $current = $(this);
        //     if ( $current.is(':first') ) {
        //         console.log('inside :first');
        //         $current.find('.element-up').addClass('disabled');
        //     }
        //     if ( $(element).is(':last') ) {
        //         console.log('inside :last');
        //         $current.find('input[class^="element-down"]').addClass('disabled');
        //     }
        // });

            // if ( $current.prev('.array-element').length ) {
            //     console.log('Previous .array-elements found. Enabling up-button on ' + index);
            //     $current.find('input[class^="element-down"]').removeClass('disabled');
            // } else {
            //     $current.find('input[class^="element-down"]').addClass('disabled');
            // }
            // if ( $current.next('.array-element').length ) {
            //     console.log('More .array-elements found. Enabling down-button on ' + index);
            //     $current.find('input[class^="element-up"]').removeClass('disabled');
            // } else {
            //     $current.find('input[class^="element-up"]').addClass('disabled');
            // }
            // if ( !$current.val() ) {
            //     $current.find('input[class^="element-up"]').removeClass('disabled');
            // }

    });

    // On submit
    $('.form').on('submit', function(e) {
        console.log($(this).serialize());
        return true;
    });

});