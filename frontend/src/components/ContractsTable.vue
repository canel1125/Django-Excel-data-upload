<template>
    <div class="container" v-if="contractSlug">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Contrato</th>
                    <th>Fecha</th>
                    <th>Origen</th>
                    <th>Destino</th>
                    <th>Moneda</th>
                    <th>Tarifa 20 GP</th>
                    <th>Tarifa 40 GP</th>
                    <th>Tarifa 40 HC</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="rate in ratesList" :key="rate.id">
                    <td>{{contractInfo['name']}}</td>
                    <td>{{contractInfo['date']}}</td>
                    <td>{{rate.origin }}</td>
                    <td>{{rate.destination }}</td>
                    <td>{{rate.currency }}</td>
                    <td>{{rate.twenty }}</td>
                    <td>{{rate.forty }}</td>
                    <td>{{rate.fortyhc }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>


<script>
import {getAPI } from '../axios-api'


export default {
  name: 'ContractsTable',
  props: ['contractSlug'],
  data(){
      return{
          ratesList: [],
          contractInfo:[]
      }
  },
    //En caso de que el valor del slug pasado como prop cambie la funcion se ejecuta y obtiene los datos de ese mismo slug
    watch:{
        contractSlug: function(val){
            if (this.contractSlug){
                //Obtengo contratos
                getAPI.get('http://127.0.0.1:8000/contracts/rates/' + this.contractSlug )
                    .then(response=> {
                        //console.log(response.data)
                        this.ratesList = response.data
                    })
                    .catch(err => {
                        console.log(err)
                    })
                //Obtengo información del contrato
                getAPI.get('http://127.0.0.1:8000/contracts/' + this.contractSlug )
                    .then(response=> {
                        this.contractInfo = response.data
                    })
                    .catch(err => {
                        console.log(err)
                    })
            }
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
