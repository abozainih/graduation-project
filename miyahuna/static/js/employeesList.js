$(document).ready(function() {
    var t = $('#employeesList').DataTable({
        responsive: true,

        language: {
            url: '//cdn.datatables.net/plug-ins/1.11.5/i18n/ar.json',
            searchPlaceholder:'ابحث عن موظف',
         },
         dom: 'Bfrtp',
         buttons: [
            {
                text: 'اضف موظف جديد',
                className:'btn btn-info btn-fw',
                action: function ( e, dt, button, config ) {
                    window.location.href = '/employees/create/';
                },
            },
                        {
                text: 'اضف موظف ادخال بيانات',
                className:'btn btn-info btn-fw',
                action: function ( e, dt, button, config ) {
                    window.location.href = '/employees/create/DataEntry/';
                },
            },



        ],

        order: [[ 1, 'asc' ]],

        columnDefs: [
          { className: "dt-center p-3 dir-ltr" , targets: "_all" },
          { "searchable": false,"orderable": false,"targets": 0},
         ],

         initComplete : function(settings, json) {
                $( "#employeesList_wrapper" ).prepend("<div id='widgits'></div");
                $(".dt-buttons").prependTo("#widgits");
                $("#employeesList_filter").prependTo("#widgits");
//                $('.dt-button').addClass('btn btn-info btn-fw');
                $( ".dt-button" ).prepend("<i class='mdi mdi-plus-thick pl-2'></i>");
                $('#widgits').addClass('align-items-baseline d-flex justify-content-between');
//                $("#create").click(function(){
//                    window.location.href="{% url 'CreateCustomer' %}";
//                });

         }
    });

    t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

    })
