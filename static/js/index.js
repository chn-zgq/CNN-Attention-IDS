function change_count(i) {
    var str = 'count_' + i;
    document.getElementById('count_0').style.display = "none";
    document.getElementById('count_1').style.display = "none";
    document.getElementById('count_2').style.display = "none";
    document.getElementById('count_3').style.display = "none";
    document.getElementById('count_4').style.display = "none";
    document.getElementById(str).style.display = "block";
}
function change_sniff() {
    setTimeout(function () {
        alert("Sniffing Done!");
        document.getElementById('pcap_table').style.display = "block";
    }
        , 3000);
}
function change_feature() {
    setTimeout(function () {
        alert("Feature Extracting Done!");
        document.getElementById('featute_scaler_table').style.display = "none";
        document.getElementById('featute_table').style.display = "block";
    }
        , 2000);
}
function change_data_preprocess() {
    setTimeout(function () {
        alert("Data Preprocessing Done!");
        document.getElementById('featute_table').style.display = "none";
        document.getElementById('featute_scaler_table').style.display = "block";
    }
        , 1500);
}
function change_data_regroup() {
    setTimeout(function () {
        alert("Data Regrouping Done!");
        document.getElementById('predict_table').style.display = "none";
        document.getElementById('data_regroup_table').style.display = "block";
    }
        , 1000);
}
function change_predict() {
    setTimeout(function () {
        alert("Intrusion Detecting Done!");
        document.getElementById('data_regroup_table').style.display = "none";
        document.getElementById('predict_table').style.display = "block";
    }
        , 3000);
}
function change_alarm() {
    document.getElementById('system_info').style.display = "none";
    document.getElementById('alarm_table').style.display = "block";
}
function change_system_info() {
    document.getElementById('alarm_table').style.display = "none";
    document.getElementById('system_info').style.display = "block";
}