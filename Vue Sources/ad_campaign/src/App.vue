<template>
    <div id="app">
      <router-view/>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
    name: "App",
    components: {
    },
    methods: {
      async setUserInfo() {
        const dataUser = await apiService("/api/user/current-user/");
        const requestUser = dataUser["email"];
        window.localStorage.setItem("email", requestUser);
      }
    },
    created() {
        this.setUserInfo();
    }
}
</script>

