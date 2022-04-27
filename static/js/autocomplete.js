// Typeahead remote-request engine
var entities = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    remote: {
        url: '/autocomplete?q=',
        prepare: function (query, settings) {
            settings.url = settings.url + encodeURIComponent(query);
            return settings;
        },
        transform: function (payload) {
            // console.log(payload);
            var responseArray = payload.result;
            var newArray = [];
            var q = $('.typeahead').val();
            // console.log(q)
            $.each(responseArray, function(i, m) {
                if (m.display.toLowerCase().indexOf(q.toLowerCase()) >= 0) {
                    // Apply icons and replace obvious sub_displays
                    if (m.domain == "people") {
                        sub = m.sub_display.replace("Person,", "");
                        icon = "icon_person";
                    } else if (m.domain == "events") {
                        // https://eloquentjavascript.net/09_regexp.html#c_ztGnSKyKy1
                        sub = m.sub_display.replace(/Begivenhed,|på Aarhus Teater/g, "");
                        icon = "icon_event";
                    } else {
                        icon = "icon_bookmark";
                    }
                    // because unable to do inplace replacements
                    m.sub_display = sub;
                    m.icon = icon;
                    newArray.push(m);
                }
            });
            return newArray;
        }
    }
});

$(document).ready(function(){
    $('.typeahead').typeahead({
        hint: false,
        highlight: true,
        minLength: 2
    },
    {
        name: 'entities',
        display: 'display',
        source: entities,
        limit: 25,
        templates: {
            suggestion: function(data) {
                if(data.hasOwnProperty('sub_display')) {
                    return '<div><p class="pre-icon ' + data.icon + '">' + data.display + '</p><p>' + data.sub_display + '</p></div>';
                } else {
                    return '<div><p class="pre-icon ' + data.icon + '">' + data.display + '</p></div>';
                }
            }
        }
    })

    .on("typeahead:select", function(e, datum) {
        var $form = $(this).closest('form');
        if ($form.hasClass('autocomplete')) {
            // window.location.href('/' + datum.domain + '/' + datum.id);
            $("input.search_input_v2").removeAttr('name');
            $form.attr('action', '/' + datum.domain + '/' + datum.id);
            $form.submit();

        } else if ($form.attr('id') == 'relation-form') {
            $form.find('input[name="object_id"]').attr('value', datum.id);
            $form.find('input[name="object_domain"]').attr('value', datum.domain);
        }
    });

});
