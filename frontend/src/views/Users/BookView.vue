<script setup>
import { ref, onMounted } from 'vue'
import Navbar from '@/components/Navbar.vue'
import axios from 'axios'

// Reactive state for books and table headers
const books = ref([])
const headers = [
  { title: 'ISBN', value: 'isbn' },
  { title: 'Title', value: 'title' },
  { title: 'Author', value: 'author' },
  { title: 'Publisher', value: 'publisher' },
  { title: 'Year Published', value: 'year_published' },
  { title: 'Available Copies', value: 'available_copies' },
]

// Fetch books on component mount
const fetchBooks = async () => {
  const response = await axios.get('http://127.0.0.1:8000/books/')
  books.value = response.data
}

// Fetch books when component is mounted
onMounted(fetchBooks)
</script>

<template>
  <Navbar />
  <v-container>
    <h2 class="text-center my-5">BOOKS</h2>
    <v-data-table :headers="headers" :items="books" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Book List</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="fetchBooks()">Refresh</v-btn>
        </v-toolbar>
      </template>
    </v-data-table>
  </v-container>
</template>
