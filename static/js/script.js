$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});

$(document).ready(function () {
    $(".alert").hide(5000);
});

$(document).ready(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/iterno/',
        method: 'GET',
        data: '',
    }).done(function (data) {
        $('#txtOrderNo').val(data[0].iter_no)
        console.log(data)
    }) 

});

// Product Name Binding Using ID::::
let ifIdInput = $('#hiddenloopcounter-1').val()
var tableOrder = document.getElementById("tableOrderDetails");
if (ifIdInput != '') {
    console.log(ifIdInput)
    for (var b = 1; b < tableOrder.rows.length - 1; b++) {
        let idInput = $('#productValue-' + b).val()
        let loopCounter = $('#hiddenloopcounter-' + b).val()
        console.table('PRODUCT ID:::', idInput, loopCounter)
        $.ajax({
            url: 'http://127.0.0.1:8000/api/update_product/' + idInput + '/',
            method: 'GET',
            data: '',
            dataType: 'json',
        }).done((data) => {
            console.log(data)
            $('#rowproductValue-' + loopCounter).text(data.product_name)
        })
    }
}

// variable declaration

var sno = 0;

var addbtn = document.getElementById("add-button-1");
var updatebtn = document.getElementById("update-button-1");

if (addbtn && updatebtn) {
    addbtn.style.display = "block";
    updatebtn.style.display = "none";
}

// Data binding

$('#ddlProdName').change(function () {
    var id = $('#ddlProdName').val();
    console.log(id);


    $.ajax({
        url: 'http://127.0.0.1:8000/api/update_product/' + id + '/',
        method: 'GET',
        data: '',
    })
        .done(function (data) {
            console.log(data)

            $.each(data, function () {
                console.log(data.unit.unit_name);
                console.log(data.product_price);
                $('#txtUnit').val(data.unit[0].unit_name);
                $('#txtPrice').val(data.product_price);
                $('#txtQuantity').val("");
                $('#txtAmount').val("");

            })
        })
})

// calculate total amount

$('#txtQuantity').keyup(function () {

    var quantity = $('#txtQuantity').val();
    var txtPrice = $('#txtPrice').val();
    var result = parseFloat(quantity * txtPrice).toFixed(2);
    console.log(result)
    $('#txtAmount').val(parseFloat(result).toFixed(2));

})

//to check

$('#txtOrderNo').keyup(function (event) {
    var currentOrderNo = $('#txtOrderNo').val();
    var quantity = $('#txtQuantity').val();
    var txtPrice = $('#txtPrice').val();
    var result = parseFloat(quantity * txtPrice).toFixed(2);
    console.log(result)
    $('#txtAmount').val(parseFloat(result).toFixed(2));

})

// loading automatic date
function loaddate() {
    var now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var days = now.getDate();
    var hrs = now.getHours();
    var min = now.getMinutes();
    var sec = now.getSeconds();
    var today = days + "-" + month + "-" + year; // + ", Time: " + hrs + "h-" + min + "m-" + sec + "s"

    // var today = year + "-" + month + "-" + days + "-" + time + "-" + min + "-" + sec;
    $('#txtOrderDate').val(today)
}

$(document).ready(function (){
    var tableOrder = document.getElementById("tableOrderDetails");
    var totalAmount = 0;
    var totalPrice = 0;
    var totalQuantity = 0;
    for (var table_data = 1; table_data < tableOrder.rows.length - 1; table_data++) {
        totalPrice = totalPrice + parseFloat(tableOrder.rows[table_data].cells[3].innerHTML)
        totalQuantity = totalQuantity + parseFloat(tableOrder.rows[table_data].cells[4].innerHTML);
        totalAmount = totalAmount + parseFloat(tableOrder.rows[table_data].cells[5].innerHTML);
    }

    document.getElementById("txtTotalPrice").innerHTML = parseFloat(totalPrice).toFixed(2);
    document.getElementById("txtTotalQuantity").innerHTML = totalQuantity;
    document.getElementById("txtTotalAmount").innerHTML = parseFloat(totalAmount).toFixed(2);
    document.getElementById("txtTotalAmt").value = parseFloat(totalAmount).toFixed(2);

});

// add products on table

function addOrders() {

    sno++;

    let rowIndex = "row-" + sno;

    var getProdName = document.getElementById("ddlProdName");
    var product = getProdName.options[getProdName.selectedIndex].text;
    //console.log("product",product)
    var productValue = document.getElementById("ddlProdName").value;

    var unit = document.getElementById("txtUnit").value;
    var price = document.getElementById("txtPrice").value;
    var quantity = document.getElementById("txtQuantity").value;
    var amount = document.getElementById("txtAmount").value;

    var table = document.getElementById('tableOrderDetails')
    var trow = table.rows.length -2;

    if (trow > 0){
        trow++
        $('#tableOrderDetails').append(
            '<tr style="text-align:center" id=' + "rowData-" + trow + '><input type=hidden value=' + productValue + ' id=' + "productValue-" + trow + '>' +
            '</td><td id=' + rowIndex + '>' + trow +
            '</td><td role="'+ productValue +'" id=' + "rowproductValue-" + trow + '>' + product +
            '</td><td id=' + "rowUnit-" + trow + '>' + unit +
            '</td><td id=' + "rowPrice-" + trow + '>' + price +
            '</td><td id=' + "rowQuantity-" + trow + '>' + quantity +
            '</td><td id=' + "rowAmount-" + trow + '>' + amount +
            '</td><td><input type="button" class="btn btn-success" onclick=editRow("' + trow + '","' + productValue + '") value="Edit"></td><td><input type="button" class="btn btn-danger" onclick=deleteRow("' + trow + '") value="Delete"></td>');
        //console.log(product);
    
    }else{

    $('#tableOrderDetails').append(
        '<tr style="text-align:center" id=' + "rowData-" + sno + '><input type=hidden value=' + productValue + ' id=' + "productValue-" + sno + '>' +
        '</td><td id=' + rowIndex + '>' + sno +
        '</td><td role="'+ productValue +'" id=' + "rowproductValue-" + sno + '>' + product +
        '</td><td id=' + "rowUnit-" + sno + '>' + unit +
        '</td><td id=' + "rowPrice-" + sno + '>' + price +
        '</td><td id=' + "rowQuantity-" + sno + '>' + quantity +
        '</td><td id=' + "rowAmount-" + sno + '>' + amount +
        '</td><td><input type="button" class="btn btn-success" onclick=editRow("' + sno + '","' + productValue + '") value="Edit"></td><td><input type="button" class="btn btn-danger" onclick=deleteRow("' + sno + '") value="Delete"></td>');
    //console.log(product);
    }
    findTotalSum()

    document.getElementById("ddlProdName").value = "0";
    $('#txtUnit').val("");
    $('#txtPrice').val("");
    $('#txtQuantity').val("");
    $('#txtAmount').val("");

    addbtn.style.display = "block";
    updatebtn.style.display = "none";

}

function findTotalSum() {
    var tableOrder = document.getElementById("tableOrderDetails");
    var totalAmount = 0;
    var totalPrice = 0;
    var totalQuantity = 0;
    for (var table_data = 1; table_data < tableOrder.rows.length - 1; table_data++) {
        totalPrice = totalPrice + parseFloat(tableOrder.rows[table_data].cells[3].innerHTML);
        totalQuantity = totalQuantity + parseFloat(tableOrder.rows[table_data].cells[4].innerHTML);
        totalAmount = totalAmount + parseFloat(tableOrder.rows[table_data].cells[5].innerHTML);
    }

    document.getElementById("txtTotalPrice").innerHTML =  parseFloat(totalPrice).toFixed(2);
    document.getElementById("txtTotalQuantity").innerHTML = totalQuantity;
    document.getElementById("txtTotalAmount").innerHTML = parseFloat(totalAmount).toFixed(2);
    document.getElementById("txtTotalAmt").value = parseFloat(totalAmount).toFixed(2);

   
}

// delete row in html table

function deleteRow(rowId) {
    document.getElementById("rowData-" + rowId).remove();
    findTotalSum()
    sno--;
   
}

// editing row in html table

function editRow(rowId, prodVal) {
    console.log("rowId", prodVal)

    if (isNaN(prodVal)){
    
        var getProdName = document.getElementById("ddlProdName");
        getProdName.options[getProdName.selectedIndex].text = prodVal
     
    }else{
        document.getElementById("ddlProdName").value = prodVal;

    }

    document.getElementById("txtUnit").value = document.getElementById("rowUnit-" + rowId).innerHTML;
    document.getElementById("txtPrice").value = document.getElementById("rowPrice-" + rowId).innerHTML;
    document.getElementById("txtQuantity").value = document.getElementById("rowQuantity-" + rowId).innerHTML;
    document.getElementById("txtAmount").value = document.getElementById("rowAmount-" + rowId).innerHTML;

    addbtn.style.display = "none";
    updatebtn.style.display = "block";

    document.getElementById("updateRow").innerText = rowId;

}

//update in html table

function updateOrders() {
    var addbtn = document.getElementById("add-button-1");
    var updatebtn = document.getElementById("update-button-1");

    addbtn.style.display = "block";
    updatebtn.style.display = "none";

    var currentRow = document.getElementById("updateRow").innerText;

    console.log("currentRow", currentRow)



    var getProdName = document.getElementById("ddlProdName");
    var product = getProdName.options[getProdName.selectedIndex].text;
    var productValue = document.getElementById("ddlProdName").value;

    document.getElementById("ddlProdName").value = product;
    document.getElementById("rowproductValue-" + currentRow).innerHTML = product;
    document.getElementById("rowUnit-" + currentRow).innerHTML = document.getElementById("txtUnit").value;
    document.getElementById("rowPrice-" + currentRow).innerHTML = document.getElementById("txtPrice").value;
    document.getElementById("rowQuantity-" + currentRow).innerHTML = document.getElementById("txtQuantity").value;
    document.getElementById("rowAmount-" + currentRow).innerHTML = document.getElementById("txtAmount").value;

    findTotalSum()


    $('#ddlProdName').val("0");
    $('#txtUnit').val("");
    $('#txtPrice').val("");
    $('#txtQuantity').val("");
    $('#txtAmount').val("");


}

//validate forms

function validateForm() {
    var x = document.forms["myform"]["ddlCustomer"].value;
    if (x == "0") {
        alert(" Customer name must be filled out");
        return false;
    }
   
    var x = document.forms["myform"]["txtTotalAmt"].value;
    if (x == "") {
        alert(" Total amount must be filled out");
        return false;
    }

    var x = document.forms["myform"]["commentDescription"].value;
    if (x == "") {
        alert(" Description name must be filled out");
        return false;
    }

    var productDetails=[];

    //gets table
    var oTable = document.getElementById('tableOrderDetails');

    //gets rows of table
    var rowLength = oTable.rows.length;
    if (rowLength <= 2){
        alert("product should be filled")
        return false;
    }

    for (var i = 1; i < rowLength - 1; i++) {
        var oCells = oTable.rows.item(i).cells;
      
        

        var dataVal = {
           
            'prod_id': oCells.item(1).role,
            'unit_ordered': oCells.item(2).innerHTML,
            'price_ordered': oCells.item(3).innerHTML,
            'quantity_ordered': oCells.item(4).innerHTML,
            'total_amount_ordered': oCells.item(5).innerHTML,
        }
        productDetails.push(dataVal);
        hiddendata = JSON.stringify(productDetails)

        $('#hiddenArray').val(hiddendata);
    }
    console.log(productDetails)
    var orderNumber = document.getElementById('txtOrderNo').value;
    // var order = orderNumber.options[orderNumber.selectedIndex].id;

    var finalOderList = {
        "order_no": orderNumber,
        "productDetails": productDetails
    }
    
}
function validateAddProduct() {
    let product = document.getElementById('ddlProdName').value;
    let quantity =  document.getElementById('txtQuantity').value;

    if (product == "0") {
        alert('Choose Product!!!');
        return false;
    }
    if (quantity == "") {
        alert('Choose Quantity!!!');
        $('#txtQuantity').attr('style', 'background: #ffe6ee; border: 1px solid #df1b1b; box-shadow: 1px 1px 12px 1px #df1b1b;')
        setTimeout(() => { if ($('#txtQuantity').length > 0) { $('#txtQuantity').attr('style', 'disabled'); } }, 2500)
        return false;
    }
    else{
        addOrders()
    }
    
}

function EditCustomerDetails(x){
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/update_customer/'+ x +'/',
        data: '',
        dataType: 'json',
    }).done(function(data){
        console.log(data)
        $('#txtCustName').val(data.customer_name);
        $('#txtPhNo').val(data.phone_number);
        $('#txtCustCity').val(data.city);  
        $('#formOrderID').attr('action', '/updatecust/'+ x +'/' );
    })
}

function EditUnitDetails(x){
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/update_unit/'+ x +'/',
        data: '',
        dataType: 'json',
    }).done(function(data){
        console.log(data)
        $('#txtUnitName').val(data.unit_name);
        $('#formOrderID').attr('action', '/updateunit/'+ x +'/' );
    })
}

function EditProdDetails(x){
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/update_product/'+ x +'/',
        data: '',
        dataType: 'json',
    }).done(function(data){
        console.log(data)
        $('#txtProName').val(data.product_name);
        $('#txtProPrice').val(data.product_price);
        $('#ddlUnitName').val(data.unit[0].unit_id);
        $('#formOrderID').attr('action', '/updateprod/'+ x +'/' );
    })
}

var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

function validateUnit() {
    let unitName = document.getElementById('txtUnitName').value;
  
    if (unitName == "") {
        alert(" Unit name must be filled out");
        return false;
    }
}

function validateprod() {
    var prodName = document.getElementById("txtProName").value;
    if (prodName == "") {
        alert(" Product name must be filled out");
        return false;
    }
    var unitName = document.getElementById("ddlUnitName").value;
    if (unitName == "0") {
        alert(" Unit name must be filled out");
        return false;
    }
    var prodPrice = document.getElementById("txtProPrice").value;
    if (prodPrice == "0") {
        alert(" Product price must be filled out");
        return false;
    }
}

function validateCust() {
    var custName = document.getElementById("txtCustName").value;
    if (custName == "") {
        alert(" Customer name must be filled out");
        return false;
    }
    var custPh = document.forms["formCreateCustomer"]["txtPhNo"].value;
    if (custPh == "") {
        alert(" Phone number must be filled out");
        return false;
    }
    var custCity = document.forms["formCreateCustomer"]["txtCustCity"].value;
    if (custCity == "") {
        alert(" City name must be filled out");
        return false;
    }
}