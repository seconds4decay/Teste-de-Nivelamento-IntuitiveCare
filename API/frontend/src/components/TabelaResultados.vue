<template>
    <div v-if="resultados.length > 0" class="resultados-container">
        <h3>Resultados</h3>
        <table>
            <thead>
            <tr>
                <th>Registro ANS</th>
                <th>CNPJ</th>
                <th>Razão Social</th>
                <th>Nome Fantasia</th>
                <th>Modalidade</th>
                <th>Logradouro</th>
                <th>Numero</th>
                <th>Complemento</th>
                <th>Bairro</th>
                <th>Cidade</th>
                <th>UF</th>
                <th>CEP</th>
                <th>DDD</th>
                <th>Telefone</th>
                <th>Fax</th>
                <th>Endereço Eletrônico</th>
                <th>Representante</th>
                <th>Cargo Representante</th>
                <th>Região de Comercialização</th>
                <th>Data Registro ANS</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(operadora, index) in resultados" :key="index">
                <td>{{ operadora.Registro_ANS }}</td>
                <td>{{ operadora.CNPJ }}</td>
                <td>{{ operadora.Razao_Social }}</td>
                <td>{{ operadora.Nome_Fantasia }}</td>
                <td>{{ operadora.Modalidade }}</td>
                <td>{{ operadora.Logradouro }}</td>
                <td>{{ operadora.Numero }}</td>
                <td>{{ operadora.Complemento }}</td>
                <td>{{ operadora.Bairro }}</td>
                <td>{{ operadora.Cidade }}</td>
                <td>{{ operadora.UF }}</td>
                <td>{{ operadora.CEP }}</td>
                <td>{{ operadora.DDD }}</td>
                <td>{{ operadora.Telefone }}</td>
                <td>{{ operadora.Fax }}</td>
                <td>{{ operadora.Endereco_Eletronico }}</td>
                <td>{{ operadora.Representante }}</td>
                <td>{{ operadora.Cargo_Representante }}</td>
                <td>{{ operadora.Regiao_Comercializacao }}</td>
                <td>{{ operadora.Data_Registro_ANS }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'

@Options({
  props: {
    resultados: Array
  }
})

export default class TabelaResultados extends Vue {
  resultados!: Array<any> 
}

</script>

<style scoped>
.resultados-container {
  margin-top: 20px;
  padding: 15px;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  overflow-x: auto;
}

h3 {
  color: #333;
  margin-bottom: 10px;
  text-align: center;
}

table {
  width: 100%;
  border-collapse: collapse;
  background: white;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #007bff;
  color: white;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

tr:hover {
  background-color: #ddd;
}

@media screen and (max-width: 768px) {
  table {
    display: block;
    overflow-x: auto;
    white-space: nowrap;
  }
}
</style>
