<template>
  <div class="container">
    <form @submit.prevent="createContract">
      <div class="row justify-content-center align-items-center">
        <div class="col-lg-5 mx-auto">
          <div class="card">
            <h3 class="mb-3">Ingresar ruta</h3>
            <div class="form-floating mb-3">
              <input type="name" class="form-control" id="floatingInput" placeholder="Nombre" v-model="contract.name" required>
              <label for="floatingInput">Nombre</label>
            </div>
            <div class="form-floating mb-3">
              <input type="date" class="form-control" id="ContractDate" name="date" v-model="contract.date" required>
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


//validar fecha front
let date = new Date().toISOString().slice(0,-14)
console.log(date); //:max

//document.getElementById("ContractDate").max = date;


export default {
  name: 'UploadForm',
  data(){
    return{
      contract: {
        'name': '',
        'date': '',
        'file': '',
      }
    }
  },
  methods:{
    createContract(){
      let selectedExcel = document.getElementById("inputFile").files[0] 
      console.log(selectedExcel)

        getAPI.get ('http://127.0.0.1:8000/contracts/rates/contrato-1')
            .then(response=> {
                console.log(response.data)
                this.ratesList = response.data
            })
            .catch(err => {
                console.log(err)
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
            //console.log(XLSX.utils.sheet_to_json(worksheet));
            this.excelRates = XLSX.utils.sheet_to_json(worksheet);
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
