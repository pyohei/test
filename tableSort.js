function createRow(id){
  var tbodyElement = document.getElementById(id).getElementsByTagName("tbody")[0];
  var trElement = document.createElement("tr");
  var tdElement = document.createElement("td");
  var tdElement2 = document.createElement("td");
  var contentNode = document.createTextNode(document.addRow.addValue.value);
  // alert(contentNode);

  tdElement.appendChild(contentNode);
  tdElement2.appendChild(document.createTextNode("t"));
  trElement.appendChild(tdElement);
  trElement.appendChild(tdElement2);
  tbodyElement.appendChild(trElement);
}

function sortNum(rowNum){
  var numList = getNums(rowNum);
  var numList = collumnSort(numList);
  // alert(numList);
  // var numLists = document.getElementById("num");
  // var numList = numLists.getElementsByTagName("tr");
  // alert(numList.item(2).cells.item(0).firstChild.nodeValue);
  //var childList = numLists.childNodes;
  // alert(childList[1].innerHTML);
  arrange(numList);
}

function getNums(row){
  var bodys = document.getElementById("sorts");
  var trList = bodys.getElementsByTagName("tr");
  var sortIndex = [];
  for (var i in trList) {
    // alert(i);
    if (i == 0){
      continue;
    }
    if (isNaN(i)){
      break;
    }
    // alert(trList[i].cells[row].firstChild.nodeValue);
    sortIndex.push(trList[i].cells[row].firstChild.nodeValue);
  }
  return sortIndex;
  // for (var trBody in trList) {
  //   alert(trBody.item(0));
  // }
//  alert(numList.item(2).cells.item(0).firstChild.nodeValue);
}

function collumnSort(rows){
  var sortList = [];
  var num = 1;
  for (var r = 0; r < rows.length; r++) {
    var o = {};
    o["order"] = num;
    o["comp"] = rows[r];
    sortList.push(o);
    // alert(o["order"]);
    // alert(o["comp"]);
    num = num + 1;
  }
  // var orgCollumn = rows;
  var results = sortList.sort(function (a, b) {
    var o, p;
    if (typeof a === 'object' && typeof b === 'object' && a && b) {
      o = a['comp'];
      p = b['comp'];
      if (o === p) {
        return 0;
      }
      if (typeof o === typeof p) {
        return o < p ? -1 : 1;
      }
      return typeof o < typeof p ? -1 : 1;
    // } else {
    //   throw {
    //     alert("error");
    //     return;
    //   };
    }
  });
  var exchangeList = [];
  for (var n = 0; n < results.length; n++){
    exchangeList.push(results[n]["order"]);
  }
  return exchangeList;
}

function arrange(orders){
  var bodys = document.getElementById("sorts");
  var trList = bodys.getElementsByTagName("tr");
  // alert(trList[1]);
  var header = trList[0].cloneNode(true);
  var clones = [];
  for (var i = 0; i < orders.length; i++) {
    clones.push(trList[orders[i]].cloneNode(true));
  }
  for (var i = 0; i < orders.length; i++){
    trList[i+1].parentNode.replaceChild(clones[i], trList[i+1]);
  }
}
/* http://d.hatena.ne.jp/sandai/20100823/p1#016 */