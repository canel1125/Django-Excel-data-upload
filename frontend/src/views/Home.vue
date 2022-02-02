<template>
  <div class="home">
    <UploadForm />
    <ContractsTable/>
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
  }
}
</script>
