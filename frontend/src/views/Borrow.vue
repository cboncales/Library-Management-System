<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Reactive state for borrowed books and table headers
const borrowedBooks = ref([])
const headers = [
  { text: 'Book Title', value: 'book_title' },
  { text: 'Borrowed Date', value: 'borrowed_date' },
  { text: 'Due Date', value: 'due_date' },
  { text: 'Returned Date', value: 'returned_date' },
  { text: 'Fine Amount', value: 'fine_amount' },
]

// Fetch borrowed books for a specific user (use actual user_id in the URL)
const fetchBorrowedBooks = async () => {
  const userId = 'some-user-uuid' // Replace with dynamic user ID
  const response = await axios.get(`http://127.0.0.1:8000/api/borrowed_books/${userId}/`)
  borrowedBooks.value = response.data
}

// Fetch borrowed books when component is mounted
onMounted(fetchBorrowedBooks)
</script>
<template>
  <v-container>
    <h2>Borrowed Books</h2>
    <v-data-table :headers="headers" :items="borrowedBooks" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Borrowed Books List</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="fetchBorrowedBooks">Refresh</v-btn>
        </v-toolbar>
      </template>
      <template v-slot:item.fine_amount="{ item }">
        <span :class="item.fine_amount > 0 ? 'text-red' : 'text-green'">{{
          item.fine_amount
        }}</span>
      </template>
    </v-data-table>
  </v-container>
</template>
