
function getClientWidth() {
    return document.body.clientWidth;
}

function getResourceWidth() {
    var el = document.getElementsByClassName("resource_wrapper")[0]; 
    if (el) {
        return el.clientWidth;
    } else {
        return 0;
    }
}

function resize() {
    var $list;
    if(getClientWidth() > breakpoint) {
        // convert page-complementary from dropdown-list to normal sidebar-list
        $list = $('.complementary--default.dropdown');
        if ($list) {
            $list.removeClass('dropdown').addClass('list--dark');
            $list.children('.dropdown_trigger').hide();
            $list.children('[class^="dropdown_list"]').addClass('complementary_inner').show();
        }
        // if collectionspage (result-list) convert search-content to default complementary on wide screens
        if ($('body').hasClass('collectionspage')) {
            $('#site-search').removeClass('complementary--transform').addClass('complementary--default');
        }

    // Small screens
    } else {
        // Convert page-complementary list in sidebar to light, dropdown list
        $list = $('.complementary--default.list--dark');
        if ($list) {
            $list.removeClass('list--dark').addClass('dropdown');
            $list.children('.dropdown_trigger').show();
            $list.children('[class^="dropdown_list"]').removeClass('complementary_inner').hide();
        }

        // if collectionspage (result-list) convert search-content to transforming complementary on small screens
        if ($('body').hasClass('collectionspage')) {
            $('#site-search').removeClass('complementary--default').addClass('complementary--transform');
        } 
    }

    // If resource is present
    if ($('body.resourcepage')) {
        var resource = getResourceWidth();
        if (resource < resourceMinBP) {
            $('.resource_wrapper dt, .resource_image').removeClass('media_left');
            $('.resource_wrapper dd, .resource_core').removeClass('media_content');
        } else {
            $('#description dt, #administration dt, .resource_image').addClass('media_left');
            $('#description dd, #administration dd, .resource_core').addClass('media_content');
            if (resource >= resourceMaxBP) {
                // $('.resource_core dt').addClass('media_left');
                // $('.resource_core dd').addClass('media_content');
                $('[class^="resource_"] dt').addClass('media_left');
                $('[class^="resource_"] dd').addClass('media_content');

            }
        }
    }

}

function initialize() {
    // Add icon to the initially checked search-option
    $('.radio_input:checked').siblings('.radio_text').addClass('icon--after icon_checked');
    resize();
}

var breakpoint = 720; // 45em * font-size (16px)
var resourceMinBP = 500;
var resourceMaxBP = 640;


function updateActionStates(el) {
    return true;
}

$(document).ready(function() {

    $('#slinky-menu').slinky();

    /* INITIALIZE */
    initialize();

    /* RESIZE */
    $(window).resize(function() {
        resize();
    });

    /* SCROLL */
    $(window).scroll(function() {    
        var scroll = $(window).scrollTop();

        /* Top-link stuff */
        if(scroll >= 400){ // Value of scrollTop is in pixels - maybe
            $(".link--tothetop").fadeIn(1000);
        }else{
            $(".link--tothetop").fadeOut(800);
        }
    });

    // Only display on testpage
    // if (window.location.pathname == "/test") {
    //     $.getJSON('https://almanak.github.io/schemas/people-full.json')
    //     .done(function(schema) {
    //         $.getJSON('/people/000113565?fmt=json')
    //             .done(function(data) {
    //                 // BrutusInForms
    //                 var BrutusinForms = brutusin["json-forms"];
    //                 bf = BrutusinForms.create(schema);
    //                 var container = document.getElementById('resourcecontainer');
    //                 bf.render(container, data);
                    
    //                 // Json-editor                   
    //                 // data.id = "000113565";
    //                 // data.type = "person";
    //                 // data.schema = "person.aarhusteater";
    //                 // var element = document.getElementById('jsoneditor');
    //                 // var options = {
    //                 //     ajax: true,
    //                 //     schema: schema,
    //                 //     startval: data,
    //                 //     theme: 'html',
    //                 //     display_required_only: false,
    //                 //     disable_collapse: false,
    //                 //     disable_edit_json: false,
    //                 //     disable_properties: false,
    //                 //     disable_array_delete_all_rows: false,
    //                 //     disable_array_delete_last_row: false,
    //                 //     // object_layout: "grid",
    //                 //     remove_empty_properties: false,
    //                 //     required_by_default: true,
    //                 //     no_additional_properties: false
    //                 // };
    //                 // editor = new JSONEditor(element, options);
    //             })
    //             .fail(function() {
    //                 console.log("Error fetching data");
    //             });
    //     })
    //     .fail(function() {
    //         console.log("Error fetching schema");
    //     });
    // }

    /*
    ** FORMS
    */


    // Cloner et repeatable felt og ændrer klassen samt værdien af feltet
    // $('#form').on('click', '.add-element', function() {
    //     console.log("add-element clicked");
    //     var newDiv = $(this).parent().clone();
    //     var inputfield = newDiv.children(":input");
    //     newDiv.children("button").removeClass('add-element').addClass('remove-element').text('-');
    //     inputfield.val('');
    //     $(this).parent().after(newDiv);
    // });

    // Fjerner et repeatable felt med remove-knap
    // $('#form').on('click', '.remove-element', function() {
    //     console.log("remove-element clicked");
    //     $(this).parent().remove();
    // });

    // On submit
    $('#form').on('submit', function(e) {
        e.preventDefault();
        console.log($(this).serialize());
    });



    /*
    ** ANCHOR-CLICKS
    */

    // Animate all clicks on internal anchors
    // http://www.paulund.co.uk/smooth-scroll-to-internal-links-with-jquery
    // https://jonsuh.com/blog/better-scroll-to-anchor-links/
    // https://css-tricks.com/snippets/jquery/smooth-scrolling/
    // I used the css-tricks edition
    $('a[href*="#"]:not([href="#"])').on('click', function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
            if (target.length) {
                if (getClientWidth() < breakpoint) {
                    offTop = target.offset().top - $(".complementary--content").outerHeight(true);
                } else {
                    offTop = target.offset().top;
                }
                $('html, body').animate({
                    scrollTop: offTop
                }, 700);
                return false;
            }
        }
    });
    
    /* Home/top links are just that - no fancy stuff */
    $('a[href="#"]').on('click', function( ) {
        $('html, body').animate({scrollTop: 0}, 500);
        return false;
    });


    /*
    ** DROPDOWN LISTS
    */
    $('.dropdown_trigger').on('click', function() {
        $(this).toggleClass('open').children('span').toggleClass('icon_arrow--down icon_arrow--up');
        $(this).siblings('[class^="dropdown_list"]').toggle(150);
        $('body').toggleClass('overlayed--20');
    });

    $('.overlay--20').on('click', function() {
        $('.dropdown_trigger.open').trigger('click');
    });

    /*
    ** ADDITIONAL ANCHOR-CLICK RULES
    */
    $('.site-header_link--default, .site-header_link--homepage, .homepage_search-link').on('click', function(e) {
        panel = $(this).attr('href');
        if (panel === '/') {
            return true;
        } else if ( $(panel).hasClass('complementary--transform') ) {
            e.preventDefault();
            $(panel).addClass('open');
            $('body').addClass('overlayed--10');
        }
        if ($(this).hasClass("homepage_search-link")) {
            $('.search_input_v2').trigger('focus');
            // console.log($(this));
        }
    });

    $('.site-header_close, .overlay--10').on('click', function(e) {
        e.preventDefault();
        // $('.site-trigger').removeClass('active');
        $('.complementary--transform').removeClass('open');
        $('body').removeClass('overlayed--10');
    });


    /*
    ** SEARCH-INPUT
    */
    $('.search_input_v2').on('focusin', function() {
        if( $(this).val().length > 1 ) {
            $('.search_help').fadeOut(200);
        } else {
            $('.search_options').fadeIn(200);
        }
    })
    .on('focusout', function() {
        $('.search_options, .search_help').fadeOut(200);
    })
    .on('keyup', function() {
        if( $(this).val().length > 1 ) {
            $('.search_options, .search_help').fadeOut(200);
        } else {
            $('.search_options').fadeIn(200);
        }
    });

    /*
    ** RADIO-OPTIONS
    */
    $('.radio_label').on('click', function() {
        var $input = $('.radio_input', this);
        var $searchIcon = $('.search_wrapper .search_icon').first();
        
        // remove current icon_class, if present
        var classList = $searchIcon.attr('class').split(" ");
        var iconIdx = classList.reIndexOf(/icon_/);
        if (iconIdx > -1) {
            $searchIcon.removeClass(classList[iconIdx]);
        }

        // add new icon_class from checked radio_input, if present
        classList = $input.attr('class').split(" ");
        iconIdx = classList.reIndexOf(/icon_/);
        if (iconIdx > -1) {
            $searchIcon.addClass(classList[iconIdx]);
        }

        // remove ALL checked attributes and ALL checked-icons
        $('.radio_input').removeAttr('checked');
        $('.radio_text').removeClass('icon--after icon_checked');

        // Add checked attribute and checked-icon on active radio-input, inside clicked radio_label
        $input.attr('checked', true).siblings('.radio_text').addClass('icon--after icon_checked');
        $('.search_help').show();
        $('.search_input').trigger('focus');
        
        // 
        return false;
    });

});
