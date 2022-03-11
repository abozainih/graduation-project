

$('#example').DataTable( {
    serverSide: true,
    ajax: {
        url :'http://127.0.0.1:8000/customers/api/list/?format=datatables',
        dataSrc:'data'
    },

//        coulmns : [
//            { data: 'customer_name' },
//            { data: 'customer_PhoneNumber' },
//            { data: 'customer_lastOrderDate' },
//            { data: 'price_per_gallon' },
//
//        ],

//        coulmns : [
//            { data: 'user.phone_number', 'name': 'user.phone_number' },
//            { data: 'user.phone_number', 'name': 'user.phone_number' },
//            { data: 'customer_lastOrderDate' },
//            { data: 'price_per_gallon' },
//
//        ],

} );