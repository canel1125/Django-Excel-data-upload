<template>
  <div class="container">
    <div class="row justify-content-center align-items-center">
      <div class="col-lg-5 mx-auto">
        <div class="card">
          <h3 class="mb-3">Ingresar ruta</h3>
          <div class="form-floating mb-3">
            <input type="name" class="form-control" id="floatingInput" placeholder="Nombre">
            <label for="floatingInput">Nombre</label>
          </div>
          <div class="form-floating mb-3">
            <input type="date" class="form-control" id="ContractDate" name="date" >
            <label for="date">Fecha del contrato:</label>
          </div>
          <div class="input-group mb-3">
            <input type="file" class="form-control" placeholder="Nombre" id="inputGroupFile02">
          </div>
          <div class="d-grid gap-2">
            <button class="btn btn-primary" type="submit">Continuar</button> 
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
//validar fecha front
let date = new Date().toISOString().slice(0,-14)
console.log(date); //:max

//document.getElementById("ContractDate").max = date;

export default {
  name: 'UploadForm',
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
