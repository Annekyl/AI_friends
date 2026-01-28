<script setup>
import {useRoute, useRouter} from "vue-router";

const route = useRoute(); // 当前url的相关信息
const router = useRouter(); // 打开新页面，后退等

// router.push({
//   name: "homepage-index"
// });
</script>

<template>
  个人空间:{{ route.params.user_id }}
</template>

<style scoped>

</style>