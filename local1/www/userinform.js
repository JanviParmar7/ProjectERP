function myfunction() {
    var e_mail = document.getElementById("emailid").value;
    alert("Welcome! " + e_mail);
    frappe.call({
        method: 'local1.www.userinform.userData',
        args: {
            'data': e_mail
        }
    }).then(r => {
        console.log(r)
    });
}