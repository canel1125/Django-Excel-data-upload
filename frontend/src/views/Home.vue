<template>
  <div class="home">
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
