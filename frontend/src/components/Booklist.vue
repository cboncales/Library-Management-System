<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Reactive state for books and table headers
const books = ref([])
const headers = ref([
  { text: 'Title', value: 'title' },
  { text: 'Author', value: 'author' },
  { text: 'ISBN', value: 'isbn' },
  { text: 'Available Copies', value: 'available_copies' },
])

console.log(headers)

// Fetch books from the backend
const fetchBooks = async () => {
  const response = await axios.get('http://127.0.0.1:8000/api/books/')
  books.value = response.data
}

// Fetch books when component is mounted
onMounted(fetchBooks)
</script>

<template>
  <v-container>
    <h2>Books</h2>
    <pre>{{ headers }}</pre>
    <v-data-table :headers="headers" :items="books" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Books Available</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="fetchBooks">Refresh</v-btn>
        </v-toolbar>
      </template>
    </v-data-table>
  </v-container>
</template>
