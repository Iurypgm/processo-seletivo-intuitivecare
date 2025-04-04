<template>
  <div class="container">
    <h1>Busca de Operadoras</h1>
    <div class="busca-wrapper">
      <input v-model="termoBusca" placeholder="Digite um termo..." />
      <button @click="buscarOperadoras">Buscar</button>
    </div>
    <ul>
      <li v-for="op in operadoras" :key="op.Registro_ANS">
        <strong>{{ op.Nome_Fantasia || op.Razao_Social }}</strong> -
        {{ op.CNPJ }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from "vue";

const termoBusca = ref("");
const operadoras = ref([]);

async function buscarOperadoras() {
  const res = await fetch(
    `http://localhost:8000/operadoras?q=${termoBusca.value}`
  );
  operadoras.value = await res.json();
}
</script>

<style scoped>
.container {
  max-width: 900px;
  width: 100%;
  margin: 2rem auto;
  padding: 1rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  word-break: break-word;
  overflow-wrap: break-word;
  text-align: center;
}

.busca-wrapper {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

input {
  padding: 0.5rem;
  width: 60%;
}

button {
  padding: 0.5rem 1rem;
}
</style>
