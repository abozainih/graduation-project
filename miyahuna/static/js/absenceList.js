$(document).ready(function() {
    var t = $('#absenceList').DataTable({
        responsive: true,
        language: {
            url: '//cdn.datatables.net/plug-ins/1.11.5/i18n/ar.json',
         },
         dom: 'rtp',

        columns: [

            null,
            null,
            {'data': 'is_paid', 'render': function(data,type,row,meta){

                if(data)
                    return "<i class='mdi mdi-check-bold badge badge-success'></i>"
                else
                    return "<i class='mdi mdi-close-thick badge badge-danger'></i>"

            }},

        ],

        order: [[ 1, 'asc' ]],

        columnDefs: [
          { className: "dt-center p-3 dir-ltr" , targets: "_all" },
          { "searchable": false,"orderable": false,"targets": 0},
         ],

         initComplete : function(settings, json) {
                $( "#absenceList_wrapper" ).prepend("<div id='widgits'></div");
                $(".dt-buttons").prependTo("#widgits");
                $("#absenceList_filter").prependTo("#widgits");
//                $('.dt-button').addClass('btn btn-info btn-fw');

         }
    });

    t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

    })
