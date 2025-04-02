<template>
    <div>
        <form @submit.prevent="enviarFormulario">
            <div>
                <label for="registro">Registro:</label>
                <input type="text" id="registro" v-model="formData.registro"/>
            </div>

            <div>
                <label for="cnpj">CNPJ:</label>
                <input type="text" id="cnpj" v-model="formData.cnpj"/>
            </div>

            <div>
                <label for="razao">Razão Social:</label>
                <input type="text" id="razao_social" v-model="formData.razao_social"/>
            </div>

            <button type="submit">Enviar</button>
        </form>

        <TabelaResultados v-if="resultados.length > 0" :resultados="resultados"></TabelaResultados>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { Options, Vue } from 'vue-class-component'
import TabelaResultados from './TabelaResultados.vue'

@Options({
    components: {
        TabelaResultados
    }
})

export default class FormBusuca extends Vue {
    formData = {
        registro: null,
        cnpj: null,
        razao_social: null
    }

    resultados = []

    async enviarFormulario () {
            this.resultados = []

            if (!this.formData.registro && !this.formData.cnpj && !this.formData.razao_social) {
                alert('Por favor, preencha pelo menos um campo.')
                return
            }

            console.log('Dados do formulário:', this.formData)

            const resposta = await axios.post('http://127.0.0.1:8000/api/buscar', this.formData)
            console.log('Resposta da API:', resposta.data)

            if (resposta.data.resultados === undefined) {
                alert('Erro: Algo deu errado ao buscar os dados.')
                return
            }

            if (resposta.data.resultados.length === 0) {
                alert('Nenhum resultado encontrado.')
                return
            }
            this.resultados = resposta.data.resultados
    }
}
</script>

<style scoped>
form {
  max-width: 400px;
  margin: 20px auto;
  padding: 15px;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

div {
  display: flex;
  flex-direction: column;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
}

input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #007bff;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #0056b3;
}

</style>
