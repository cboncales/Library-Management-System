<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Reactive state for books and table headers
const books = ref([])
const headers = [
  { text: 'Title', value: 'title' },
  { text: 'Author', value: 'author' },
  { text: 'Available Copies', value: 'available_copies' },
]

// Fetch books on component mount
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
    <v-data-table :headers="headers" :items="books" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Book List</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="fetchBooks">Refresh</v-btn>
        </v-toolbar>
      </template>
    </v-data-table>
  </v-container>
</template>
