<template>
    <div class="container">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Contrato</th>
                    <th>Origen</th>
                    <th>Destino</th>
                    <th>Moneda</th>
                    <th>tw</th>
                    <th>ft</th>
                    <th>ftw</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="rate in ratesList" :key="rate.id">
                    <td>{{rate.id }}</td>
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
  data(){
      return{
          ratesList: []
      }
  },
    created(){
        getAPI.get('http://127.0.0.1:8000/contracts/rates/1')
            .then(response=> {
                console.log(response.data)
                this.ratesList = response.data
            })
            .catch(err => {
                console.log(err)
            })
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
