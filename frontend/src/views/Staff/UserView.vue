<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Reactive state for users and table headers
const users = ref([])
const headers = [
  { title: 'Username', value: 'username' },
  { title: 'Email', value: 'email' },
  { title: 'Role', value: 'role' },
]

// Fetch users from the backend
const fetchUsers = async () => {
  const response = await axios.get('http://127.0.0.1:8000/users/')
  users.value = response.data
}

// Fetch users when component is mounted
onMounted(fetchUsers)
</script>
<template>
  <v-container>
    <h2>Users</h2>
    <v-data-table :headers="headers" :items="users" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>User List</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="fetchUsers">Refresh</v-btn>
        </v-toolbar>
      </template>
    </v-data-table>
  </v-container>
</template>
