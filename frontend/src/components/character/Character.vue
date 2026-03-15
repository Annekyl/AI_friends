<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user.js'
import UpdateIcon from "@/components/character/icons/UpdateIcon.vue";
import RemoveIcon from "@/components/character/icons/RemoveIcon.vue";
import api from "@/js/http/api.js";

const props = defineProps(['character', 'canEdit'])
const emit = defineEmits(['remove'])
const user = useUserStore()
const isHover = ref(false)

async function handleRemoveCharacter() {
    try {
        const res = await api.post('/api/create/character/remove/', {
            character_id: props.character.id
        })
        if (res.data.result === 'success') {
            emit('remove', props.character.id)
        }
    } catch (err) {
        // console.log(err)
    }
}
</script>

<template>
    <div>
        <div class="avatar cursor-pointer" @mouseenter="isHover = true" @mouseleave="isHover = false">
            <div class="w-60 h-100 rounded-2xl rounded-2xl relative">
                <img :src="character.background_image" class="transition-transform duration-300"
                    :class="{ 'scale-120': isHover }" alt="">
                <div class="absolute top-50 left-0 w-60 h-50 bg-linear-to-t from-black/40 to-transparent"></div>

                <div v-if="canEdit && character?.author?.user_id === user.id" class="absolute right-0 top-50">
                    <RouterLink :to="{ name: 'update-character', params: { character_id: character.id } }"
                        class="btn btn-ghost btn-circle bg-transparent">
                        <UpdateIcon />
                    </RouterLink>

                    <button class="btn btn-ghost btn-circle bg-transparent" @click="handleRemoveCharacter">
                        <RemoveIcon />
                    </button>
                </div>

                <div class="absolute left-4 top-54 avater">
                    <div class="w-16 h-16 rounded-full ring-3 ring-white overflow-hidden">
                        <img :src="character.photo" class="w-full h-full object-cover" alt="">
                    </div>
                </div>

                <div class="absolute left-24 right-4 top-58 text-white font-bold line-clamp-1 break-all">
                    {{ character.name }}
                </div>

                <div class="absolute left-4 right-4 top-72 text-white line-clamp-4 break-all">
                    {{ character.profile }}
                </div>

            </div>
        </div>

        <RouterLink :to="{name:'user-space-index',params:{user_id:character.author.user_id}}" class="flex items-center mt-4 gap-2 w-60">
            <div class="avater">
                <div class="w-7 h-7 rounded-full overflow-hidden">
                    <img :src="character.author.photo" class="w-full h-full object-cover" alt="">
                </div>
            </div>
            <div class="text-sm font-bold line-clamp-1 break-all">
                {{ character.author.username }}
            </div>

        </RouterLink>

    </div>
</template>

<style scoped></style>