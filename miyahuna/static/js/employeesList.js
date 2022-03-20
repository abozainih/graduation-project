$(document).ready(function() {
    var t = $('#employeesList').DataTable({
        responsive: true,

        columns : [
            null,
            null,
            null,
            null,
            null,
            null,
            {'data': 'employee_update_link', 'render': function(data,type,row,meta){

                return `
                    <div>
                    <a data-tool="tooltip" data-placement="top" title="اظهار سجلات غياب الموظف" href="${row.absence_url}"><button class="btn btn-dark btn-sm mdi mdi-history">
                      </button> </a>
                    <button data-toggle="modal" data-target="#addAbsence" data-tool="tooltip" data-placement="top" title="اضف غياب" data-url="${row.add_absence_url}" class="addAbsence btn btn-sm btn-success mdi mdi-plus-thick"></button>
                      <a data-tool="tooltip" data-placement="top" title="تعديل بيانات الموظف" href="${row.employee_update_link}"><button class="btn btn-info btn-sm mdi mdi-note-edit">
                      </button> </a>
                    </div>
                    `;
            }},

        ],
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
                $('[data-tool="tooltip"]').tooltip({ trigger :'hover' });
                $('.addAbsence').click(function(){
                     $(".forms-sample").attr("action", $(this).attr('data-url'));
                })
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
