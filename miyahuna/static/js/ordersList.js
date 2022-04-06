$(document).ready(function() {
    var t = $('#ordersList').DataTable({
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
            null,
            {'data': 'order_total_price', 'render': function(data,type,row,meta){

                return "<label class='badge badge-info'>" + row.order_status_name + "</label>"
            }
            },
            {'data': 'order_total_price', 'render': function(data,type,row,meta){

                return data + "<i class='mdi mdi-currency-ils px-1'> </i>"
            }
            },
            null,
            {'data': 'actions', 'render': function(data,type,row,meta){

                return `
                    <div>
                        <button data-toggle="modal" data-target="#rejectOrder" data-tool="tooltip" data-placement="top" title="الغاء الطلب" data-url="${row.reject_order_url}" class="btn btn-sm btn-danger mdi mdi-delete"></button>
                        <button data-toggle="modal" data-target="#acceptOrder" data-tool="tooltip" data-placement="top" title="تأكيد الطلب" data-url="${row.accept_order_url}" class="btn btn-sm btn-success mdi mdi-check-bold"></button>
                    </div>
                    `;
            }},

        ],
         buttons: [

            {
                text: 'اضف طلب جديد',
                className:'btn btn-success plus dt-button',
                action: function ( e, dt, button, config ) {
                    window.location.href = '/orders/create/';
                },
            },
            {
                text: 'عرض سجل الطلبات',
                className:'btn btn-dark history dt-button',
                action: function ( e, dt, button, config ) {
                    window.location.href = '/orders/history/';
                },
            },
        ],

        order: [[ 1, 'asc' ]],

        columnDefs: [
          { className: "dt-center p-3 dir-ltr" , targets: "_all" },
          { "searchable": false,"orderable": false,"targets": 0},
         ],

         initComplete : function(settings, json) {
                $( "#ordersList_wrapper" ).prepend("<div id='widgits'></div");
                $(".dt-buttons").prependTo("#widgits");
                $("#ordersList_filter").prependTo("#widgits");
                $( ".plus" ).prepend("<i class='mdi mdi-plus-thick pl-2'></i>");
                $( ".history" ).prepend("<i class='mdi mdi-history pl-2'></i>");
                $('#widgits').addClass('align-items-baseline d-flex justify-content-end');
                $('[data-tool="tooltip"]').tooltip({ trigger :'hover' });
                $('[data-target="#acceptOrder"]').click(function(){
                     $(".forms-sample").attr("action", $(this).attr('data-url'));
                });
                $('[data-target="#rejectOrder"]').click(function(){
                     $(".forms-sample2").attr("action", $(this).attr('data-url'));
                })

         }
    });

    t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

    })
