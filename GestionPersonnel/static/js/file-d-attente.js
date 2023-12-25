var doctSpeciality = document.getElementById('doctSpeciality').value;
var customerLookingFor = document.querySelectorAll('.customerLookingFor')
var Ligne = document.querySelectorAll('.userLine')

for (var i = 0; i < customerLookingFor.length; i++ )
{
    var elt = customerLookingFor[i].value;
    
    if(elt != doctSpeciality)
        Ligne[i].style.display = "None";
    
}