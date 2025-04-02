<template>
  <h1>Busca na Lista de Cadastros de Operadoras</h1>
  <FormBusca></FormBusca>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import FormBusca from './components/FormBusca.vue'

@Options({
components: {
FormBusca
}
})
export default class App extends Vue {}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
