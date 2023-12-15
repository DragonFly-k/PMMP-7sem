using System.Collections;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.SceneManagement;

public class PlayerMovement : MonoBehaviour
{
    public void LoadScene(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
    }
    public float speed = 15f;
    public CharacterController controller;
    public Transform groundCheck;
    public LayerMask groundMask;
    public float gravity = -9.8f;
    public float groundDistance = 0.4f;
    public float jumpHeight = 3f;

    private Vector3 velocity;
    private bool isGrounded;

    public TextMeshProUGUI collectedText;
    private int collectedCount = 0;

    void Update()
    {
        isGrounded = Physics.CheckSphere(groundCheck.position, groundDistance, groundMask);

        if (isGrounded && velocity.y < 0)
        {
            velocity.y = -2f;
        }

        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");

        Vector3 move = transform.right * x + transform.forward * z;
        controller.Move(move * speed * Time.deltaTime);

        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            LoadScene("menu");
        }
    }

    private void OnControllerColliderHit(ControllerColliderHit hit)
    {
        if (hit.collider.CompareTag("Collectible"))
        {
            Destroy(hit.collider.gameObject);
            collectedCount++;
            UpdateCollectedText();
        }
    }

    private void UpdateCollectedText()
    {
        if (collectedText != null)
        {
            collectedText.text = "Collected: " + collectedCount.ToString();
        }
    }
}
