<template>
  <div class="home">
    <div class="alert alert-success alert-dismissible" v-if="uploadedSlug">
      <strong>Información guardada! </strong> La información se almacenó correctamente.
    </div>
    <UploadForm v-on:emitedSlug=" getSlug($event)"/>
    <ContractsTable :contractSlug=uploadedSlug />
  </div>
</template>

<script>
// @ is an alias to /src
import UploadForm from '@/components/UploadForm.vue'
import ContractsTable from '@/components/ContractsTable.vue'


export default {
  name: 'Home',
  components: {
    UploadForm,
    ContractsTable
  },
  data(){
    return{
      uploadedSlug: false
    }
  },
  methods:{
    getSlug: function(value){
      this.uploadedSlug = value;
    }
  }
}
</script>
