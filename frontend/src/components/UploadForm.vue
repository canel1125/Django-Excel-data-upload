<template>
  <div class="container">
    <form @submit.prevent="createContract" method="POST">
      <div class="row justify-content-center align-items-center">
        <div class="col-lg-5 mx-auto">
          <div class="card">
            <h3 class="mb-3">Ingresar ruta</h3>
            <div class="form-floating mb-3">
              <input type="name" class="form-control" id="ContractName" placeholder="Nombre" v-model="contract.name" required :max="date">
              <label for="floatingInput">Nombre</label>
            </div>
            <div class="form-floating mb-3">
              <input type="date" class="form-control" id="ContractDate" name="date" v-model="contract.date" v-bind:max="date"  required>
              <label for="date">Fecha del contrato:</label>
            </div>
            <div class="input-group mb-3">
              <input type="file" class="form-control" placeholder="Nombre" id="inputFile" accept=".xls,.xlsx" required @change="excelToJson">
            </div>
            <div class="d-grid gap-2">
              <button class="btn btn-primary" type="submit">Continuar</button> 
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>


<script>
import {getAPI } from '../axios-api'
import XLSX from 'xlsx';


//Variable date donde voy a guardar la fecha actual para validar que no se ingrese una fecha futura por front
let date = new Date().toISOString().slice(0,-14)

var excelRates =[];

export default {
  name: 'UploadForm',
  data(){
    return{
      date,
      contract: {
        'name': '',
        'date': '',
      }
    }
  },
  methods:{
    createContract(){      
      let formData = {

      }
    
      formData.name = document.getElementById('ContractName').value
      formData.date = document.getElementById('ContractDate').value
      formData.rates = excelRates
      formData.csrfmiddlewaretoken ='{{csrf_token}}' // 3

      getAPI.post('/contracts/create_contract/', formData)
        .then(response=> {
          if (response.data.status == "Success") {
            console.log("El formulario se subió exitosamente");
          }
        })
        .catch(err => {
          console.log(err);
        })
    },

    excelToJson(e) {
      var files = e.target.files, f = files[0];
      var reader = new FileReader();
      reader.onload = function(e) {
        var data = new Uint8Array(e.target.result);
        var workbook = XLSX.read(data, {type: 'array'});
        let sheetName = workbook.SheetNames[0]
        let worksheet = workbook.Sheets[sheetName];
        let excelJsonArray = XLSX.utils.sheet_to_json(worksheet)

        //Lista de columnas innecesarias del excel
        let unwantedColumns=["ETT","20'FR","20'OT","20'TK","40'FH","40'FR","40'OH","40'OT","40'RH","40'RH_1","Routing"];
        excelJsonArray.forEach(rate => {
          for (let i = 0; i < unwantedColumns.length; i++) {
            delete rate[unwantedColumns[i]];
          }
        });
        excelRates = excelJsonArray;
        //console.log(excelRates);
      };
      reader.readAsArrayBuffer(f);
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.card{
    padding: 30px;
    border-radius: 1rem
}
</style>
