var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["السبت","الاحد","الاثنين","الثلاثاء","الاربعاء","الخميس","الجمعه"],
        datasets: [{
            label: ' عدد الطلبات بالاسبوع الماضي    ',
            data: [55,23,11,23,61,33,5],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

var ctx1 = document.getElementById('myChart2');
var myChart = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['يناير', 'فبراير', 'مارس', 'ابريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'],
        datasets: [{
            label: 'عددالطلبات بالاشهر',
            data: [112, 219, 31, 533, 211, 443,111,222,333,444,555,666],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

$(function() {

    var start = moment().startOf('month');
    var end = moment().endOf('month');

    function cb(start, end) {
        $('#reportrange span').html(start.format('D-MM-YYYY') + ' - ' + end.format('D-MM-YYYY'));
        $.ajax({url: "orders/sales/"+start.format('YYYY-MM-DD')+"/"+end.format('YYYY-MM-DD'), success: function(result){
                 jQuery({ Counter: 0 }).animate({ Counter: result.ordersSales }, {
                    duration: 1000,
                    easing: 'swing',
                    step: function () {
                      $("#sales").text(Math.ceil(this.Counter));
                    }
                  });
           }});
    }

    $('#reportrange').daterangepicker({

        "showDropdowns": true,
        "minYear": 2000,
        "autoApply": true,
        ranges: {
            'Today': [moment(), moment()],
            'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            'Last 7 Days': [moment().subtract(6, 'days'), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month': [moment().startOf('month'), moment().endOf('month')],
            'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        },

        "startDate": moment().subtract(1, 'days'),
        "endDate": moment().subtract(1, 'days'),
        "opens": "left",
        "maxDate": moment(),
        "drops": "auto"
    }, function(start, end, label) {
        $('#reportrange span').html(start.format('D-MM-YYYY') + ' - ' + end.format('D-MM-YYYY'));

           $.ajax({url: "orders/sales/"+start.format('YYYY-MM-DD')+"/"+end.format('YYYY-MM-DD'), success: function(result){
                 jQuery({ Counter: 0 }).animate({ Counter: result.ordersSales }, {
                    duration: 1000,
                    easing: 'swing',
                    step: function () {
                      $("#sales").text(Math.ceil(this.Counter));
                    }
                  });
           }});
        }
    );

    cb(start, end);
    $('.counter').each(function(){
         var $this = $(this);
         jQuery({ Counter: 0 }).animate({ Counter: $this.attr('data-value') }, {
            duration: 1000,
            easing: 'swing',
            step: function () {
               $this.text(Math.ceil(this.Counter));
            }
         });

    });
});


