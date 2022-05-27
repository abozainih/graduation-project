$(document).ready(function() {
    var t = $('#ordersHistory').DataTable({
        searching: false,
        responsive: true,
        language: {
            url: '//cdn.datatables.net/plug-ins/1.11.5/i18n/ar.json',
         },
         dom: 'Bfrtp',

         columns : [
            null,
            null,
            null,
            {'data': 'order_status', 'render': function(data,type,row,meta){
                if(row.order_status == 0)
                    return "<label class='badge badge-info'>" + row.order_status_name + "</label>"
                else if(row.order_status == 1)
                    return "<label class='badge badge-success'>" + row.order_status_name + "</label>"
                else
                    return "<label class='badge badge-danger'>" + row.order_status_name + "</label>"
            }
            },
            {'data': 'order_total_price', 'render': function(data,type,row,meta){

                return data + "<i class='mdi mdi-currency-ils px-1'> </i>"
            }},
        ],
                 buttons: [

            {
                text: 'اضف طلب جديد',
                className:'btn btn-success plus dt-button',
                action: function ( e, dt, button, config ) {
                    window.location.href = '/orders/Customer/create/';
                },
            }],
        order: [[ 1, 'asc' ]],

        columnDefs: [
          { className: "dt-center p-3 dir-ltr" , targets: "_all" },
          { "searchable": false,"orderable": false,"targets": 0},
         ],

         initComplete : function(settings, json) {
                $( "#ordersHistory_wrapper" ).prepend("<div id='widgits'></div");
                $(".dt-buttons").prependTo("#widgits");
                $("#ordersHistory_filter").prependTo("#widgits");
                $( ".plus" ).prepend("<i class='mdi mdi-plus-thick pl-2'></i>");
                $('#widgits').addClass('align-items-baseline d-flex justify-content-end');
                $('[data-tool="tooltip"]').tooltip({ trigger :'hover' });
         }

    });

    t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

    })
