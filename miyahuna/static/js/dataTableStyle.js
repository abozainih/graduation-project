$(document).ready(function() {
    var t = $('#customersList').DataTable({
        responsive: true,
        language: {
            url: '//cdn.datatables.net/plug-ins/1.11.5/i18n/ar.json',
            searchPlaceholder:'ابحث عن مشترك',
         },
         dom: 'Bfrtp',
         buttons: [
            {
                text: 'اضف مشترك جديد',
                className:'btn btn-info btn-fw',
                attr: {
                    'data-toggle' :'modal',
                    'data-target' :"#addCustomer"
                }
            }
        ],

        order: [[ 1, 'asc' ]],

        columnDefs: [
          { className: "dt-center p-3", targets: "_all" },
          { "searchable": false,"orderable": false,"targets": 0}
         ],

         initComplete : function(settings, json) {
                $( "#customersList_wrapper" ).prepend("<div id='widgits'></div");
                $(".dt-buttons").prependTo("#widgits");
                $("#customersList_filter").prependTo("#widgits");
//                $('.dt-button').addClass('btn btn-info btn-fw');
                $( ".dt-button" ).prepend("<i class='mdi mdi-plus-thick pl-2'></i>");
                $('#widgits').addClass('align-items-baseline d-flex justify-content-between');
         }
    });

    t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

    })
