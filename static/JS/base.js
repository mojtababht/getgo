// var myMap = new L.Map('map', {
//         key: 'service.03aa018ac2c2439c9270d67fb8282bfd',
//         maptype: 'dreamy',
//         poi: true,
//         traffic: false,
//         center: [35.699739, 51.338097],
//         zoom: 14
//     });


var map = L.map('map').setView([35.699739, 51.338097], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
}).addTo(map);


let sIcon = L.icon({
    iconUrl: '../static/image/LocationIcon1.png',
    iconSize: [32, 38],
    iconAnchor: [22, 94],
    popupAnchor: [-3, -76],
    shadowUrl: 'my-icon-shadow.png',
    shadowSize: [32, 38],
    shadowAnchor: [22, 94]
})
let dIcon = L.icon({
    iconUrl: '../static/image/LocationIcon2.png',
    iconSize: [32, 38],
    iconAnchor: [22, 94],
    popupAnchor: [-3, -76],
    shadowUrl: 'my-icon-shadow.png',
    shadowSize: [32, 38],
    shadowAnchor: [22, 94]
})
let sMarker = L.marker([35.699739, 51.338097], {icon: sIcon}).addTo(map);
sMarker.dragging.enable();


let dMarker = L.marker([35.689739, 51.328097], {icon: dIcon}).addTo(map);
dMarker.dragging.enable();


$(document).ready(() => {
    $('.leaflet-marker-pane').mouseup(() => {
        $('#slat').val(sMarker._latlng.lat);
        $('#slong').val(sMarker._latlng.lng);
        $('#dlat').val(dMarker._latlng.lat);
        $('#dlong').val(dMarker._latlng.lng);

    })

    $('#id_type').addClass('dropdownBtn')
    $('#id_weight').addClass('dropdownBtn')
    $('#calcprice').mouseup(() => {
        $('.warning').remove()
        if ($('#slat').val()) {
            if ($('#id_type').val() == 'regular') {
                $.ajax({
                    url: 'https://api.neshan.org/v4/direction/no-traffic?&type=car&origin=' + sMarker._latlng.lat + ',' + sMarker._latlng.lng + '&destination=' + dMarker._latlng.lat + ',' + dMarker._latlng.lng,
                    type: 'GET',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader('Api-Key', 'service.03aa018ac2c2439c9270d67fb8282bfd');
                    },
                    success: function (data) {
                        if ($('#id_weight').val() == 'small')
                            $('#price').val(data.routes[0].legs[0].duration.value * 20)
                        else if ($('#id_weight').val() == 'normal')
                            $('#price').val(data.routes[0].legs[0].duration.value * 30)
                        else if ($('#id_weight').val() == 'large')
                            $('#price').val(data.routes[0].legs[0].duration.value * 40)


                    }
                });
            } else if ($('#id_type').val() == 'instance') {
                $.ajax({
                    url: 'https://api.neshan.org/v4/direction?&type=car&origin=' + sMarker._latlng.lat + ',' + sMarker._latlng.lng + '&destination=' + dMarker._latlng.lat + ',' + dMarker._latlng.lng,
                    type: 'GET',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader('Api-Key', 'service.03aa018ac2c2439c9270d67fb8282bfd');
                    },
                    success: function (data) {
                        if ($('#id_weight').val() == 'small')
                            $('#price').val(data.routes[0].legs[0].duration.value * 25)
                        else if ($('#id_weight').val() == 'normal')
                            $('#price').val(data.routes[0].legs[0].duration.value * 35)
                        else if ($('#id_weight').val() == 'large')
                            $('#price').val(data.routes[0].legs[0].duration.value * 45)


                    }
                })
            }
        }
        else {
            $('#wrapperTotalMap').after(`
            <div class="warning">مبدا و مقصد را مشخص کنید</div>
            `)
        }
        if (!$('#id_type').val()){
            $('#wrapperTotalMap').after(`
            <div class="warning">نوع ارسال را مشخص کنید</div>
            `)
        }
         if (!$('#id_weight').val()){
            $('#wrapperTotalMap').after(`
            <div class="warning">اندازه بسته را مشخص کنید</div>
            `)
         }
    })



})


