function buildTable(data){
  var table = document.getElementById("breeds-list")

  for (var i = 0; i < data.length; i++){
    var row = <tr>
                <td>${data[i].name}</td>

    </tr>
  }
}